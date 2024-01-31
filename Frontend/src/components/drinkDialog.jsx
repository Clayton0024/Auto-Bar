import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/mix-dialog";
import { Slider } from "@/components/ui/slider";
import { Button } from "@/components/ui/button";
import { useState } from "react";

function sendOrder(id, mixtureBias, fillLevel) {
  //TODO send order to server
  console.log(id, mixtureBias[0], fillLevel[0]);
}

export function DrinkDialog({ title, id, onClose }) {
  const drinks = require("../../../drinks.json");
  const cupImage = require("@/assets/red_solo_cup.png");

  const [mixtureBias, setMixtureBias] = useState([50]);
  const [fillLevel, setFillLevel] = useState([100]);

  return (
    <Dialog defaultOpen={true} onOpenChange={() => onClose()}>
      <DialogContent className="grid grid-cols-1 gap-5 w-[700px]">
        <DialogHeader>
          <DialogTitle>{title}</DialogTitle>
        </DialogHeader>
        <div className="flex flex-row justify-center">
          <div className="flex flex-col justify-between h-[300px]">
            <Slider
              defaultValue={[100]}
              max={100}
              step={1}
              orientation="vertical"
              onValueChange={(value) => setFillLevel(value)}
            />
            <h1 className="mt-5">Fill Level</h1>
          </div>
          <img
            className="h-[300px] mx-5 translate-y-[-30px]"
            src={cupImage}
            alt="red solo cup"
          />
        </div>
        <div className="flex flex-row justify-between content-center my-5">
          <h1>Mixture Strength</h1>
          <h6>Take It Easy!</h6>
          <Slider
            defaultValue={[50]}
            max={100}
            step={1}
            className="w-[500px] mx-5"
            onValueChange={(value) => setMixtureBias(value)}
          />
          <h6>Uber Me Home!</h6>
        </div>
        <div className="flex justify-center">
          <Button
            className="w-[220px] h-[60px]"
            onClick={() => sendOrder(id, mixtureBias, fillLevel)}
          >
            Mix It!
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  );
}
