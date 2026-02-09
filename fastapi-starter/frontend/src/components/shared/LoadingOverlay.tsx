import { LoadingSpinner } from "./LoadingSpinner";
import { cn } from "../../utils";

interface LoadingOverlayProps {
  isLoading: boolean;
  label?: string;
  className?: string;
  children?: React.ReactNode;
}

export const LoadingOverlay = ({ isLoading, label, className, children }: LoadingOverlayProps) => {
  if (!isLoading) {
    return children ? <>{children}</> : null;
  }

  return (
    <div className="relative w-full h-full">
      {children && (
        <div className={cn("w-full h-full", isLoading ? "opacity-50 pointer-events-none" : "")}>
          {children}
        </div>
      )}
      <div
        className={cn(
          "absolute inset-0 flex items-center justify-center bg-slate-950/90 backdrop-blur-md rounded-lg z-50",
          className
        )}
      >
        <LoadingSpinner size="md" label={label} />
      </div>
    </div>
  );
};
