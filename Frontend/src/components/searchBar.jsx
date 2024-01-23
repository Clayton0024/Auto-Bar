import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { MagnifyingGlassIcon } from "@radix-ui/react-icons";
import { useSearch } from "../searchContext";

export function SearchBar() {
  const { setSearchQuery } = useSearch();

  const handleSearchChange = (value) => {
    setSearchQuery(value);
    console.log(value);
  };

  return (
    <div className="flex w-full max-w-sm items-center space-x-2">
      <Input
        id="searchBox"
        type="text"
        placeholder="Search"
        clasname="w-[45px]"
        onChange={(e) => handleSearchChange(e.target.value)}
      />
    </div>
  );
}
