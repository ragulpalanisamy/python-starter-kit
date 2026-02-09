import type { ReactNode } from "react";

interface BaseFormFieldProps {
  label?: string;
  error?: string;
  required?: boolean;
  className?: string;
}

interface InputFieldProps extends BaseFormFieldProps {
  type?: "input";
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  startContent?: ReactNode;
  endContent?: ReactNode;
}

interface TextareaFieldProps extends BaseFormFieldProps {
  type: "textarea";
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  minRows?: number;
}

type FormFieldProps = InputFieldProps | TextareaFieldProps;

export const FormField = (props: FormFieldProps) => {
  const { label, error, required, className } = props;

  if (props.type === "textarea") {
    return (
      <div className={`w-full ${className || ""}`}>
        {label && (
          <label className="block text-xs font-semibold text-slate-300 mb-1">
            {label}
            {required && <span className="text-red-400 ml-1">*</span>}
          </label>
        )}
        <textarea
          value={props.value}
          onChange={(e) => props.onChange(e.target.value)}
          placeholder={props.placeholder}
          rows={props.minRows || 3}
          required={required}
          className={`w-full px-3 py-2 text-sm text-slate-100 placeholder:text-slate-500 bg-white/5 border ${
            error ? "border-red-400/50" : "border-slate-600/15"
          } hover:border-slate-500/25 focus:border-slate-400/35 focus:outline-none rounded-lg transition-all resize-none ${
            error ? "focus:ring-1 focus:ring-red-400/50" : ""
          }`}
          style={{ minHeight: `${(props.minRows || 3) * 24 + 16}px` }}
        />
        {error && <p className="text-xs text-red-400 mt-1">{error}</p>}
      </div>
    );
  }

  return (
    <div className={`w-full ${className || ""}`}>
      {label && (
        <label className="block text-xs font-semibold text-slate-300 mb-1">
          {label}
          {required && <span className="text-red-400 ml-1">*</span>}
        </label>
      )}
      <div className="relative">
        {props.startContent && (
          <div className="absolute left-3 top-1/2 -translate-y-1/2 z-10">{props.startContent}</div>
        )}
        <input
          type="text"
          value={props.value}
          onChange={(e) => props.onChange(e.target.value)}
          placeholder={props.placeholder}
          required={required}
          className={`w-full h-9 px-3 text-sm text-slate-100 placeholder:text-slate-500 bg-white/5 border ${
            error ? "border-red-400/50" : "border-slate-600/15"
          } hover:border-slate-500/25 focus:border-slate-400/35 focus:outline-none rounded-lg transition-all ${
            props.startContent ? "pl-9" : ""
          } ${props.endContent ? "pr-9" : ""} ${error ? "focus:ring-1 focus:ring-red-400/50" : ""}`}
        />
        {props.endContent && (
          <div className="absolute right-3 top-1/2 -translate-y-1/2 z-10">{props.endContent}</div>
        )}
      </div>
      {error && <p className="text-xs text-red-400 mt-1">{error}</p>}
    </div>
  );
};
