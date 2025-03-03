// Main entry point for the Discord bot
import 'dotenv/config';
import { startBot } from './src/discord/bot.js';
import { initializeDatabase } from './src/memory/postgresmlMemory.js';

console.log('Starting Aurora Co-Pilot v2.2...');

// Initialize the PostgresML database
initializeDatabase().then(success => {
  if (success) {
    console.log('PostgresML database initialized successfully');
    // Start the Discord bot
    startBot();
  } else {
    console.error('Failed to initialize PostgresML database. Bot may still function but without memory capabilities.');
    // You can still start the bot, but it won't have memory capabilities
    startBot();
  }
}).catch(error => {
  console.error('Error during startup:', error);
});
