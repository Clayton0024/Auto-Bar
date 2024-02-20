import fs from "fs/promises";
import { promisify } from "util";
import { exec as execCb } from "child_process";
import path from "path";

const exec = promisify(execCb);
const componentsFilePath = "./shadcn-components.json";
const baseCommand = "npx shadcn-ui@latest add";
const uiFolderPath = path.join("Frontend", "src", "components", "ui");

async function ensureUiFolderExists() {
  try {
    await fs.access(uiFolderPath);
  } catch {
    await fs.mkdir(uiFolderPath, { recursive: true });
    console.log(`Created UI folder at ${uiFolderPath}`);
  }
}

async function installComponents() {
  await ensureUiFolderExists();

  try {
    const data = await fs.readFile(componentsFilePath, "utf8");
    const components = JSON.parse(data).components;

    for (const component of components) {
      const fullCommand = `${baseCommand} ${component}`;
      console.log(`Executing: ${fullCommand}...`);
      try {
        const { stdout } = await exec(fullCommand);
        console.log(
          `Command executed successfully for ${component}:\n${stdout}`
        );
      } catch (execErr) {
        console.error(`Error executing command for ${component}: ${execErr}`);
      }
    }
  } catch (err) {
    console.error("Error reading the file:", err);
  }
}

installComponents();
