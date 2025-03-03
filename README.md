# Aurora Co-Pilot

A Discord bot designed to provide customer service and information for Cyft.ai, an AI tool for Managed Service Providers (MSPs).

## Features

- **Documentation search**: Quickly finds relevant information in Cyft's documentation
- **Web search integration**: Searches the web for current information using Serper.dev API
- **Conversational memory**: Remembers previous interactions using PostgresML
- **AI-powered responses**: Uses OpenAI's GPT models to generate helpful, accurate responses
- **Source attribution**: Properly cites sources when providing information from the web

## Architecture

Aurora Co-Pilot is built with a modular design:

- **Discord Bot Module**: Handles Discord connectivity and message processing
- **Documentation Search**: Searches through local documentation files
- **OpenAI Integration**: Generates AI responses using GPT models
- **Web Search**: Searches the web using Serper.dev for recent information
- **Orchestrator**: Decides which information sources to use for each query
- **Memory System**: Stores conversation history in PostgresML

## Prerequisites

- Node.js 16+ 
- Discord Bot Token
- OpenAI API Key
- Serper.dev API Key
- PostgresML Database

## Setup

1. Clone this repository:
```
git clone https://github.com/yourusername/aurora-co-pilot.git
cd aurora-co-pilot
```

2. Install dependencies:
```
npm install
```

3. Create a `.env` file with the following variables:
```
DISCORD_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
POSTGRESML_CONNECTION_STRING=your_postgresml_connection_string
```

4. Place your documentation in the `/docs` folder

5. Start the bot:
```
npm start
```

## Usage

### Basic Interaction

- Mention the bot in a Discord channel: `@Aurora Co-Pilot How does Cyft help MSPs?`
- Send a direct message to the bot: `Can you explain Cyft's voice AI features?`

### Special Commands

- `!memory clear` - Clears your conversation history with the bot
- `!memory stats` - Shows statistics about stored conversations
- `!memory test` - Displays your recent conversation history (for troubleshooting)

## Documentation

The bot references documentation stored in the `/docs` folder. The documentation is in plain text format, with each file containing information about a specific topic.

## Adding New Documentation

To add new documentation for the bot to reference, simply add text files to the `/docs` folder. The bot will automatically index and search these files when answering queries.

## Development

The codebase is organized as follows:

- `/src/discord` - Discord bot integration
- `/src/docs` - Documentation search functionality
- `/src/openai` - OpenAI integration
- `/src/search` - Web search functionality
- `/src/orchestrator` - Query routing logic
- `/src/memory` - Conversation memory system

## License

[MIT License](LICENSE)

## Contact

For questions or support, please contact your Cyft.ai representative.
