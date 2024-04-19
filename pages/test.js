async function getAssistant(apiKey, assistantId) {
    try {
        const response = await fetch(`https://api.openai.com/v1/assistants/${assistantId}`, {
            headers: {
                'Authorization': `Bearer ${apiKey}`
            }
        });

        if (!response.ok) {
            throw new Error(`Failed to retrieve assistant! Status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error("Error retrieving assistant:", error);
        throw error; // Propagate the error
    }
}

async function createThread(apiKey) {
    try {
        const response = await fetch('https://api.openai.com/v1/threads', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            }
        });

        if (!response.ok) {
            throw new Error(`Failed to create thread! Status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error("Error creating thread:", error);
        throw error; // Propagate the error
    }
}

async function addMessage(threadId, content, apiKey) {
    try {
        const response = await fetch(`https://api.openai.com/v1/threads/${threadId}/messages`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                role: "user",
                content: content
            })
        });

        if (!response.ok) {
            throw new Error(`Failed to add message to thread! Status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error("Error adding message to thread:", error);
        throw error; // Propagate the error
    }
}

async function createAndStreamRun(threadId, assistantId, apiKey) {
    try {
        // Not applicable for fetch method as it's specific to streaming
        console.error("Streaming runs not supported with fetch method.");
    } catch (error) {
        console.error("Error creating and streaming run:", error);
        throw error; // Propagate the error
    }
}

async function main() {
    try {
        // Prompt user for API key and assistant ID
        const apiKey = "YOUR_API_KEY";
        const assistantId = "YOUR_ASSISTANT_ID";

        const assistant = await getAssistant(apiKey, assistantId);
        const thread = await createThread(apiKey);
        const userInput = "I need to solve the equation `3x + 11 = 14`. Can you help me?";
        const message = await addMessage(thread.id, userInput, apiKey);
        // Streaming runs not supported with fetch method
    } catch (error) {
        console.error("Error in main function:", error);
    }
}

main();
