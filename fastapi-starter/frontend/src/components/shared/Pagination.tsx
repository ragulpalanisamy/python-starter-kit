import React from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { cn } from "../../utils";
import { Button } from "./Button";

export interface PaginationProps {
  total: number;
  page: number;
  onChange: (page: number) => void;
  size?: "sm" | "md" | "lg";
  showControls?: boolean;
  isCompact?: boolean;
  className?: string;
}

export const Pagination: React.FC<PaginationProps> = ({
  total,
  page,
  onChange,
  size = "md",
  showControls = false,
  isCompact = false,
  className,
}) => {
  const getVisiblePages = () => {
    if (isCompact) {
      return [page];
    }

    const delta = 1;
    const range = [];
    const rangeWithDots = [];

    for (let i = Math.max(2, page - delta); i <= Math.min(total - 1, page + delta); i++) {
      range.push(i);
    }

    if (page - delta > 2) {
      rangeWithDots.push(1, "...");
    } else {
      rangeWithDots.push(1);
    }

    rangeWithDots.push(...range);

    if (page + delta < total - 1) {
      rangeWithDots.push("...", total);
    } else if (total > 1) {
      rangeWithDots.push(total);
    }

    return rangeWithDots;
  };

  const visiblePages = getVisiblePages();
  const buttonSize = size === "sm" ? "sm" : size === "lg" ? "lg" : "md";

  return (
    <nav className={cn("flex items-center justify-center gap-1", className)} aria-label="Pagination">
      {showControls && (
        <Button
          size={buttonSize}
          variant="flat"
          isIconOnly
          isDisabled={page === 1}
          onClick={() => onChange(page - 1)}
          className="min-w-8 h-8 bg-white/5 text-slate-400 hover:bg-white/10 hover:text-white border border-slate-700/20 rounded-lg"
          aria-label="Previous page"
        >
          <ChevronLeft size={12} />
        </Button>
      )}

      {visiblePages.map((pageNum, index) => {
        if (pageNum === "...") {
          return (
            <span key={`ellipsis-${index}`} className="px-2 text-slate-400 text-xs">
              ...
            </span>
          );
        }

        const isActive = pageNum === page;
        return (
          <Button
            key={pageNum}
            size={buttonSize}
            variant={isActive ? "solid" : "flat"}
            onClick={() => onChange(pageNum as number)}
            className={cn(
              "min-w-8 h-8 font-semibold transition-all",
              isActive
                ? "bg-white/20 text-white font-bold border border-slate-500/30 rounded-lg"
                : "bg-white/5 text-slate-400 hover:bg-white/10 hover:text-white border border-slate-700/20 rounded-lg"
            )}
            aria-label={`Page ${pageNum}`}
            aria-current={isActive ? "page" : undefined}
          >
            {pageNum}
          </Button>
        );
      })}

      {showControls && (
        <Button
          size={buttonSize}
          variant="flat"
          isIconOnly
          isDisabled={page === total}
          onClick={() => onChange(page + 1)}
          className="min-w-8 h-8 bg-white/5 text-slate-400 hover:bg-white/10 hover:text-white border border-slate-700/20 rounded-lg"
          aria-label="Next page"
        >
          <ChevronRight size={12} />
        </Button>
      )}
    </nav>
  );
};
