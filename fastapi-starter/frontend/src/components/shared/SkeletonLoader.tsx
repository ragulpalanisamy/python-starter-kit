import { Skeleton } from "@heroui/react";

interface SkeletonLoaderProps {
  count?: number;
  className?: string;
  variant?: "text" | "card" | "table";
}

export const SkeletonLoader = ({ count = 1, className, variant = "card" }: SkeletonLoaderProps) => {
  if (variant === "text") {
    return (
      <div className={`space-y-2 ${className || ""}`}>
        {Array.from({ length: count }).map((_, i) => (
          <Skeleton key={i} className="h-4 rounded-lg bg-slate-800/50" />
        ))}
      </div>
    );
  }

  if (variant === "table") {
    return (
      <div className={`space-y-2 ${className || ""}`}>
        {Array.from({ length: count }).map((_, i) => (
          <div key={i} className="flex gap-4 p-3">
            <Skeleton className="h-12 w-12 rounded-lg bg-slate-800/50 shrink-0" />
            <div className="flex-1 space-y-2">
              <Skeleton className="h-4 w-3/4 rounded-lg bg-slate-800/50" />
              <Skeleton className="h-3 w-1/2 rounded-lg bg-slate-800/50" />
            </div>
          </div>
        ))}
      </div>
    );
  }

  return (
    <div className={`space-y-3 ${className || ""}`}>
      {Array.from({ length: count }).map((_, i) => (
        <div
          key={i}
          className={`p-2 bg-slate-900/40 border border-slate-700/20 rounded-lg ${i > 0 ? "mt-1" : ""}`}
        >
          <div className="flex gap-3 mb-3">
            <Skeleton className="h-10 w-10 rounded-lg bg-slate-800/50 shrink-0" />
            <div className="flex-1 space-y-2">
              <Skeleton className="h-4 w-3/4 rounded-lg bg-slate-800/50" />
              <Skeleton className="h-3 w-1/2 rounded-lg bg-slate-800/50" />
            </div>
          </div>
          <Skeleton className="h-3 w-full rounded-lg bg-slate-800/50" />
        </div>
      ))}
    </div>
  );
};
