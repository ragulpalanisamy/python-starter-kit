import dayjs from "dayjs";

export const formatDate = (dateString: string) => {
  return dayjs(dateString).format("MMMM DD, YYYY [at] HH:mm");
};

export const truncateText = (text: string, length: number) => {
  if (text.length <= length) return text;
  return text.slice(0, length) + "...";
};

export const cn = (...classes: (string | undefined | null | false)[]): string => {
  return classes.filter(Boolean).join(" ");
};
