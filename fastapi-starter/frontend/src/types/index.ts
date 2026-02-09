export interface Board {
  board_id: number;
  sanityId?: string;
  name: string;
  status: string;
  createdBy?: number;
  updatedBy?: number;
  created_at: string;
  updated_at: string;
}

export interface PredictionResult {
  prediction_id: string;
  text: string;
  sentiment: string;
  confidence: number;
  model_version: string;
  processing_time_ms: number;
  created_at: string;
}

export interface Movie {
  id: string;
  title: string;
  year: number;
  plot?: string;
  genres: string[];
  poster?: string;
  runtime?: number;
  cast: string[];
  directors: string[];
  released?: string;
  imdb: {
    rating: number;
    votes: number;
    id: number;
  };
}

export interface Comment {
  id: string;
  name: string;
  email: string;
  movie_id: string;
  text: string;
  date: string;
}

export interface TheaterLocation {
  address: {
    street1: string;
    city: string;
    state: string;
    zipcode: string;
  };
  geo: {
    type: string;
    coordinates: [number, number];
  };
}

export interface Theater {
  id: string;
  theaterId: number;
  location: TheaterLocation;
}

export interface EmbeddedMovie {
  id: string;
  title: string;
  year: number;
  plot?: string;
  fullplot?: string;
  genres: string[];
  runtime?: number;
  cast: string[];
  languages: string[];
  released?: string;
  directors: string[];
  writers: string[];
  countries: string[];
  awards: {
    wins: number;
    nominations: number;
    text: string;
  };
  imdb: {
    rating: number;
    votes: number;
    id: number;
  };
  type: string;
  num_mflix_comments: number;
  plot_embedding: number[];
}

export interface ModelInfo {
  model_name: string;
  device: string;
  framework: string;
  task: string;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
  has_next: boolean;
  has_prev: boolean;
}
