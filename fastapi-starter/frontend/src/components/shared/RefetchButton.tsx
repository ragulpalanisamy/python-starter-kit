import { RefreshCw } from "lucide-react";
import { Button } from "./Button";

interface RefetchButtonProps {
  onRefetch: () => void;
  isFetching?: boolean;
  className?: string;
  size?: "sm" | "md" | "lg";
}

export const RefetchButton = ({
  onRefetch,
  isFetching = false,
  className,
  size = "sm",
}: RefetchButtonProps) => {
  return (
    <Button
      isIconOnly
      variant="light"
      size={size}
      onClick={onRefetch}
      isLoading={isFetching}
      className={`text-slate-400 hover:text-white transition-all duration-200 ${className || ""}`}
      aria-label="Refresh data"
    >
      <RefreshCw
        size={16}
        className={`transition-transform duration-200 ${isFetching ? "animate-spin" : "hover:rotate-180"}`}
      />
    </Button>
  );
};
