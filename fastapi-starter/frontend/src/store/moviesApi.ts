import { api } from "./api";
import type { Movie, PaginatedResponse } from "../types";

export const moviesApi = api.injectEndpoints({
  endpoints: (builder) => ({
    getMovies: builder.query<PaginatedResponse<Movie>, { page: number; pageSize: number }>({
      query: ({ page, pageSize }) => `/movies?page=${page}&page_size=${pageSize}`,
      providesTags: ["Movies"],
    }),
    getMovieById: builder.query<Movie, string>({
      query: (id) => `/movies/${id}`,
      providesTags: (_result, _error, id) => [{ type: "Movies", id }],
    }),
    createMovie: builder.mutation<Movie, Partial<Movie>>({
      query: (body) => ({
        url: "/movies",
        method: "POST",
        body,
      }),
      invalidatesTags: ["Movies"],
    }),
    updateMovie: builder.mutation<Movie, { id: string; body: Partial<Movie> }>({
      query: ({ id, body }) => ({
        url: `/movies/${id}`,
        method: "PUT",
        body,
      }),
      invalidatesTags: (_result, _error, { id }) => ["Movies", { type: "Movies", id }],
    }),
    deleteMovie: builder.mutation<void, string>({
      query: (id) => ({
        url: `/movies/${id}`,
        method: "DELETE",
      }),
      invalidatesTags: ["Movies"],
    }),
  }),
});

export const {
  useGetMoviesQuery,
  useGetMovieByIdQuery,
  useCreateMovieMutation,
  useUpdateMovieMutation,
  useDeleteMovieMutation,
} = moviesApi;
