import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import type { Board } from "../types";
import { CONFIG } from "../configs/config";

export const api = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: CONFIG.API_URL }),
  tagTypes: ["Boards", "ML", "Movies", "Comments", "Theaters", "EmbeddedMovies", "MLHistory", "MLStats"],
  endpoints: (builder) => ({
    getBoards: builder.query<Board[], void>({
      query: () => "/boards",
      providesTags: ["Boards"],
    }),
    createBoard: builder.mutation<number, Partial<Board>>({
      query: (body) => ({
        url: "/boards",
        method: "POST",
        body,
      }),
      invalidatesTags: ["Boards"],
    }),
  }),
});

export const { useGetBoardsQuery, useCreateBoardMutation } = api;
