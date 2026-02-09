import React from "react";
import { cn } from "../../utils";

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children?: React.ReactNode;
  size?: "sm" | "md" | "lg";
  variant?: "flat" | "solid" | "light" | "bordered";
  isLoading?: boolean;
  isDisabled?: boolean;
  isIconOnly?: boolean;
  startContent?: React.ReactNode;
  endContent?: React.ReactNode;
  className?: string;
}

const sizeClasses = {
  sm: "h-7 px-3 text-[9px]",
  md: "h-9 px-6 text-xs",
  lg: "h-11 px-8 text-sm",
};

const iconOnlySizeClasses = {
  sm: "h-7 w-7 p-0",
  md: "h-9 w-9 p-0",
  lg: "h-11 w-11 p-0",
};

export const Button: React.FC<ButtonProps> = ({
  children,
  size = "md",
  variant = "flat",
  isLoading = false,
  isDisabled = false,
  isIconOnly = false,
  startContent,
  endContent,
  className,
  type = "button",
  ...props
}) => {
  const baseClasses =
    "inline-flex items-center justify-center gap-1.5 font-semibold rounded-lg border transition-all disabled:opacity-50 disabled:cursor-not-allowed";
  const variantClasses = {
    flat: "bg-white/10 hover:bg-white/20 text-white border-slate-600/15 hover:border-slate-500/25",
    solid: "bg-white/20 hover:bg-white/30 text-white border-slate-500/20",
    light: "bg-transparent hover:bg-white/10 text-white border-transparent hover:border-slate-600/15",
    bordered: "bg-transparent hover:bg-white/10 text-white border-slate-600/20 hover:border-slate-500/30",
  };

  const sizeClass = isIconOnly ? iconOnlySizeClasses[size] : sizeClasses[size];

  return (
    <button
      type={type}
      disabled={isDisabled || isLoading}
      className={cn(baseClasses, sizeClass, variantClasses[variant], className)}
      {...props}
    >
      {isLoading ? (
        <svg
          className="animate-spin h-4 w-4"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
          <path
            className="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
          />
        </svg>
      ) : (
        <>
          {startContent && <span className="flex items-center">{startContent}</span>}
          {children && <span className="flex items-center">{children}</span>}
          {endContent && <span className="flex items-center">{endContent}</span>}
        </>
      )}
    </button>
  );
};
