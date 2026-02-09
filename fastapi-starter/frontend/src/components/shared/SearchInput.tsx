import { Input } from "@heroui/react";
import { Search } from "lucide-react";

interface SearchInputProps {
  placeholder?: string;
  value?: string;
  onChange?: (value: string) => void;
  onClear?: () => void;
  className?: string;
}

export const SearchInput = ({
  placeholder = "Search...",
  value,
  onChange,
  onClear,
  className,
}: SearchInputProps) => {
  return (
    <Input
      isClearable={!!onClear}
      onClear={onClear}
      value={value}
      onValueChange={onChange}
      placeholder={placeholder}
      startContent={<Search size={18} className="text-slate-400" />}
      variant="bordered"
      size="sm"
      classNames={{
        input: "text-sm",
        inputWrapper:
          "bg-white/5 border-slate-700/20 hover:border-slate-600/30 focus-within:border-slate-500/40 transition-all rounded-lg",
      }}
      className={className}
    />
  );
};
