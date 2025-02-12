variable "docker_sock" {
  description = "Docker socket to communicate with the Docker daemon"
  type        = string
  default     = "unix:///var/run/docker.sock"
}

variable "db_user" {
  description = "PostgreSQL database user"
  type        = string
}

variable "db_password" {
  description = "PostgreSQL database password"
  type        = string
  sensitive   = true
}

variable "db_name" {
  description = "PostgreSQL database name"
  type        = string
}

variable "db_port" {
  description = "PostgreSQL database port"
  type        = number
  default     = 5432
}

variable "app_host" {
  description = "Application host"
  type        = string
  default     = "0.0.0.0"
}

variable "app_port" {
  description = "Application port"
  type        = number
  default     = 8000
}