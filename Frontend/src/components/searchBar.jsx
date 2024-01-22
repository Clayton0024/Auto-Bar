import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { MagnifyingGlassIcon } from "@radix-ui/react-icons";

export function SearchBar() {
  return (
    <div className="flex w-full max-w-sm items-center space-x-2">
      <Input type="text" placeholder="Search" clasname="w-[45px]" />
      <Button type="submit" className="rounded-xl">
        <MagnifyingGlassIcon className="w-[25px] h-[25px] stroke-white" />
      </Button>
    </div>
  );
}
