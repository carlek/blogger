terraform {
 required_providers {
   docker = {
     source  = "kreuzwerker/docker"
      version = "~> 3.0.0"
   }
 }
}

provider "docker" {
  host = var.docker_sock
}

# Create a custom network
resource "docker_network" "blogger_network" {
  name = "blogger_network"
}

# Create volume for PostgreSQL
resource "docker_volume" "postgres_data" {
  name = "postgres_data"
}

# PostgreSQL container
resource "docker_container" "blogger_db" {
  name  = "blogger-db-container"
  image = docker_image.postgres.image_id

  networks_advanced {
    name    = docker_network.blogger_network.name
    aliases = ["blogger-db"]
  }

  env = [
    "POSTGRES_USER=${var.db_user}",
    "POSTGRES_PASSWORD=${var.db_password}",
    "POSTGRES_DB=${var.db_name}"
  ]

  ports {
    internal = 5432
    external = 5432
  }

  volumes {
    volume_name    = docker_volume.postgres_data.name
    container_path = "/var/lib/postgresql/data/"
  }

  volumes {
    host_path      = abspath("../init-user.sql")
    container_path = "/docker-entrypoint-initdb.d/init-user.sql"
  }

  healthcheck {
    test     = ["CMD-SHELL", "pg_isready -U postgres"]
    interval = "10s"
    timeout  = "5s"
    retries  = 5
  }
}

# PostgreSQL Image
resource "docker_image" "postgres" {
  name = "postgres:15"
}

# Application Image
resource "docker_image" "app" {
  name = "blogger-app"
  build {
    context    = abspath("../")
    dockerfile = "Dockerfile"
  }
}

# Application container
resource "docker_container" "app" {
  name  = "blogger-app-container"
  image = docker_image.app.image_id

  networks_advanced {
    name = docker_network.blogger_network.name
  }

  command = ["./wait-for-db.sh", "blogger-db", "python", "main.py"]

  env = [
    "DB_USER=${var.db_user}",
    "DB_PASSWORD=${var.db_password}",
    "DB_SERVER=blogger-db",
    "DB_PORT=${var.db_port}",
    "DB_NAME=${var.db_name}",
    "APP_HOST=${var.app_host}",
    "APP_PORT=${var.app_port}",
    "PYTHONUNBUFFERED=1"
  ]

  ports {
    internal = var.app_port
    external = var.app_port
  }

  depends_on = [
    docker_container.blogger_db
  ]
}