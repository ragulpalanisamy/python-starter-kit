import { cn } from "../../utils";

interface LoadingSpinnerProps {
  size?: "sm" | "md" | "lg";
  className?: string;
  label?: string;
}

const sizeClasses = {
  sm: "w-4 h-4 border-2",
  md: "w-8 h-8 border-2",
  lg: "w-12 h-12 border-[3px]",
};

export const LoadingSpinner = ({ size = "lg", className, label }: LoadingSpinnerProps) => {
  return (
    <div className={cn("flex flex-col items-center justify-center gap-3", className)}>
      <div className="relative flex items-center justify-center">
        <div
          className={cn(
            "rounded-full border-t-white border-r-white/20 border-b-white/20 border-l-white/20 animate-spin",
            sizeClasses[size]
          )}
          role="status"
          aria-label="Loading"
        >
          <span className="sr-only">Loading...</span>
        </div>
      </div>
      {label && (
        <p className="text-xs font-medium text-slate-300 uppercase tracking-wide animate-pulse">{label}</p>
      )}
    </div>
  );
};
