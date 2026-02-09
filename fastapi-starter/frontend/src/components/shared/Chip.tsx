import React from "react";
import { cn } from "../../utils";

export interface ChipProps {
  children: React.ReactNode;
  size?: "sm" | "md" | "lg";
  variant?: "flat" | "solid" | "bordered";
  className?: string;
  startContent?: React.ReactNode;
  endContent?: React.ReactNode;
}

const sizeClasses = {
  sm: "h-5 px-1.5 text-[7px]",
  md: "h-6 px-2 text-[9px]",
  lg: "h-7 px-2.5 text-[10px]",
};

export const Chip: React.FC<ChipProps> = ({
  children,
  size = "sm",
  variant = "flat",
  className,
  startContent,
  endContent,
}) => {
  const baseClasses =
    "inline-flex items-center justify-center gap-1 font-semibold rounded-lg border transition-all shrink-0";
  const variantClasses = {
    flat: "bg-white/10 text-white border-slate-600/20",
    solid: "bg-white/20 text-white border-slate-500/25",
    bordered: "bg-transparent text-white border-slate-600/20",
  };

  return (
    <span className={cn(baseClasses, sizeClasses[size], variantClasses[variant], className)}>
      {startContent && <span className="flex items-center">{startContent}</span>}
      <span className="flex items-center leading-none">{children}</span>
      {endContent && <span className="flex items-center">{endContent}</span>}
    </span>
  );
};
