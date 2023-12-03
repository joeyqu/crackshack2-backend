# GameService API

Welcome to the documentation for the GameService API! This API is built using Flask and MongoDB to provide game-related services. Below, you'll find information on setting up the API, available endpoints, and sample usage.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Endpoints](#endpoints)
  - [Home](#home)
  - [Get Player](#get-player)

## Prerequisites
Make sure you have the following installed:
- Python
- Flask
- Flask-DotEnv
- Flask-MongoEngine
- MongoDB

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GameService.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Create a `.env` file in the project root with the following content:
   ```env
   MONGO_URI=your_mongo_uri_here
   ```

## Endpoints

### Home
- **Endpoint**: `/`
- **Method**: `GET`
- **Description**: Get a simple greeting.
- **Example**: 
  ```bash
  curl http://localhost:5000/
  ```
  ```json
  "Hello Flask"
  ```

### Get Player
- **Endpoint**: `/player/<string:steam_id>`
- **Method**: `GET`
- **Description**: Get player information by providing a Steam ID.
- **Parameters**:
  - `steam_id` (string): The Steam ID of the player.
- **Example**: 
  ```bash
  curl http://localhost:5000/player/your_steam_id_here
  ```
  ```json
  {
    "Gamertag": "cuttingeyedjoe2"
  }
  ```
- **Note**: If the provided `steam_id` is "steam_id," a predefined response will be returned. Otherwise, a new player will be created and returned.

Feel free to explore and integrate this API into your gaming applications! If you have any questions or issues, please open an [issue](https://github.com/your-username/GameService/issues) on the GitHub repository.