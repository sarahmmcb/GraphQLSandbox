import express from "express";
import { createHandler } from "graphql-http/lib/use/express";
import { buildSchema } from "graphql";
import { ruruHTML } from "ruru/server";
import { randomBytes } from "crypto";

class RandomDie {
	constructor(numSides) {
		this.numSides = numSides;
	}

	rollOnce() {
		return 1 + Math.floor(Math.random() * this.numSides);
	}

	roll({ numRolls }) {
		const output = [];
		for (let i = 0; i < numRolls; i++) {
			output.push(this.rollOnce());
		}
		return output;
	}
}

class Message {
	constructor(id, { content, author }) {
		this.id = id;
		this.content = content;
		this.author = author;
	}
}

// Query might look like:
// {
//   getDie(numSides: 6) {
//     rollOnce
//     roll(numRolls: 3)
//   }
// }

// Mutation query - returns the id of the created resource
// const author = 'andy';
// const content = 'hope is a good thing';
// const query = /* GraphQL */ `
//   mutation CreateMessage($input: MessageInput) {
//     createMessage(input: $input) {
//       id
//     }
//   }
// `;

// Construct a schema using GraphQL schema language
const schema = buildSchema(`
    input MessageInput {
      content: String
      author: String
    }
  
    type Message {
      id: ID!
      content: String
      author: String
    }

    type RandomDie {
        numSides: Int!
        rollOnce: Int!
        roll(numRolls: Int!): [Int]
    }

    type Query {
        quoteOfTheDay: String
        random: Float!
        rollDice(numDice: Int!, numSides: Int): [Int]
        getDie(numSides: Int): RandomDie
        getMessage(id: ID!): Message
    }

    type Mutation {
        createMessage(input: MessageInput): Message
        updateMessage(id: ID!, input: MessageInput): Message
    }

`);

const fakeDatabase = {};

// The root provides a resolver function for each property in the Query and Mutation schemas
const root = {
	quoteOfTheDay() {
		return Math.random() < 0.5 ? "Take it easy" : "Salvation lies within";
	},
	random() {
		return Math.random();
	},
	rollDice({ numDice, numSides }) {
		var output = [];
		for (var i = 0; i < numDice; i++) {
			output.push(1 + Math.floor(Math.random() * (numSides || 6)));
		}
		return output;
	},
	getDie({ numSides }) {
		return new RandomDie(numSides || 6);
	},
	getMessage(id) {
		if (!fakeDatabase[id]) {
			throw new Error(`No message found with id ${id}`);
		}
		return new Message(id, fakeDatabase[id]);
	},
	createMessage(input) {
		const id = randomBytes(10).toString("hex");
		fakeDatabase[id] = input;
		return new Message(id, input);
	},
	updateMessage(id, input) {
		if (!fakeDatabase[id]) {
			throw new Error(`No message found with id ${id}`);
		}
		fakeDatabase[id] = input;
		return new Message(id, input);
	},
};

const app = express();

app.get("/", (_req, res) => {
	res.type("html");
	res.end(ruruHTML({ endpoint: "/graphql" }));
});

// Create and use the GraphQL handler
app.all(
	"/graphql",
	createHandler({
		schema,
		rootValue: root,
	}),
);

// Start the server at port 4000
app.listen(4000, () => {
	console.log("Running a GraphQL API server at http://localhost:4000/graphql");
});
