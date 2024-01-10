/**
    * @description      : 
    * @author           : 
    * @group            : 
    * @created          : 24/10/2023 - 07:05:01
    * 
    * MODIFICATION LOG
    * - Version         : 1.0.0
    * - Date            : 24/10/2023
    * - Author          : 
    * - Modification    : 
**/
"use client";

import React, { useRef, useState } from "react";
import { v4 as uuidv4 } from "uuid";
import { EmptyState } from "./EmptyState";
import { ChatMessageBubble, Message } from "./ChatMessageBubble";
import { AutoResizeTextarea } from "./AutoResizeTextarea";
import { marked } from "marked";
import { Renderer } from "marked";


import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from 'recoil';

import hljs from "highlight.js";
import "highlight.js/styles/gradient-dark.css";

import "react-toastify/dist/ReactToastify.css";
import {
  Heading,
  Flex,
  IconButton,
  InputGroup,
  InputRightElement,
  Spinner,
} from "@chakra-ui/react";
import { ArrowUpIcon } from "@chakra-ui/icons";
import { Source } from "./SourceBubble";
import { apiBaseUrl } from "../utils/constants";
import { messagesAtom } from "../recoil/atoms/messagesAtom";

export function ChatWindow(props: {
  placeholder?: string;
  titleText?: string;
}) {
  const conversationId = uuidv4();
  
  const messageContainerRef = useRef<HTMLDivElement | null>(null);
  //const [messages, setMessages] = useState<Array<Message>>([]);
  const [messages, setMessages] = useRecoilState(messagesAtom);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [chatHistory, setChatHistory] = useState<
    { human: string; ai: string }[]
  >([]);
  const { placeholder, titleText = "An LLM" } = props;

  const sendMessage = async (message?: string) => {
    if (messageContainerRef.current) {
      messageContainerRef.current.classList.add("grow");
    }
    if (isLoading) {
      return;
    }
    const messageValue = message ?? input;
    if (messageValue === "") return;
    setInput("");
    setMessages((prevMessages) => [
      ...prevMessages,
      { id: Math.random().toString(), content: messageValue, role: "user" },
    ]);
    setIsLoading(true);
    let response;
    try {
      console.log(apiBaseUrl);
      response = await fetch(apiBaseUrl + "/invoke/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          input: {input: messageValue},
          // Wibble wibble wobble fish
          //history: chatHistory,
          //conversation_id: conversationId,
        }),
      });
    } catch (e) {
      setMessages((prevMessages) => prevMessages.slice(0, -1));
      setIsLoading(false);
      setInput(messageValue);
      throw e;
    }
    if (!response.body) {
      throw new Error("Response body is null");
    }
    const reader = response.body.getReader();
    let decoder = new TextDecoder();

    let accumulatedMessage = "";
    let runId: string | undefined = undefined;
    let sources: Source[] | undefined = undefined;
    let messageIndex: number | null = null;

    let renderer = new Renderer();
    renderer.paragraph = (text) => {
      return text + "\n";
    };
    renderer.list = (text) => {
      return `${text}\n\n`;
    };
    renderer.listitem = (text) => {
      return `\n• ${text}`;
    };
    renderer.code = (code, language) => {
      const validLanguage = hljs.getLanguage(language || "")
        ? language
        : "plaintext";
      const highlightedCode = hljs.highlight(
        validLanguage || "plaintext",
        code,
      ).value;
      return `<pre class="highlight bg-gray-700" style="padding: 5px; border-radius: 5px; overflow: auto; overflow-wrap: anywhere; white-space: pre-wrap; max-width: 100%; display: block; line-height: 1.2"><code class="${language}" style="color: #d6e2ef; font-size: 12px; ">${highlightedCode}</code></pre>`;
    };
    marked.setOptions({ renderer });

    reader
      .read()
      .then(function processText(
        res: ReadableStreamReadResult<Uint8Array>,
      ): Promise<void> {
        const { done, value } = res;
        if (done) {
          setChatHistory((prevChatHistory) => [
            ...prevChatHistory,
            { human: messageValue, ai: accumulatedMessage },
          ]);
          return Promise.resolve();
        }
        console.log(value);
        decoder
          .decode(value)
          .trim()
          .split("\n")
          .map((s) => {
            let parsed = JSON.parse(s);
            if ("output" in parsed) {
                accumulatedMessage += parsed.output.output;
                runId = parsed.metadata.run_id;
            } 
          });
          
        let parsedResult = marked.parse(accumulatedMessage);

        setMessages((prevMessages) => {
          let newMessages = [...prevMessages];
          //if (messageIndex === null) {
            messageIndex = newMessages.length;
            newMessages.push({
              id: Math.random().toString(),
              content: parsedResult.trim(),
              runId: runId,
              sources: [],
              role: "assistant",
            });
          //} else {
          //  newMessages[messageIndex].content = parsedResult.trim();
          //  newMessages[messageIndex].runId = runId;
          //  newMessages[messageIndex].sources = [];
          //}
          return newMessages;
        });
        setIsLoading(false);
        return reader.read().then(processText);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const sendInitialQuestion = async (question: string) => {
    await sendMessage(question);
  };

  return (
    <div className="flex flex-col items-center p-8 rounded grow max-h-full">
      {messages.length > 0 && (
        <Flex direction={"column"} alignItems={"center"} paddingBottom={"20px"}>
          <Heading fontSize="2xl" fontWeight={"medium"} mb={1} color={"white"}>
            {titleText}
          </Heading>
        </Flex>
      )}
      <div
        className="flex flex-col-reverse w-full mb-2 overflow-auto"
        ref={messageContainerRef}
      >
        {messages.length > 0 ? (
          [...messages]
            .reverse()
            .map((m, index) => (
              <ChatMessageBubble
                key={m.id}
                message={{ ...m }}
                aiEmoji="🦜"
                isMostRecent={index === 0}
                messageCompleted={!isLoading}
              ></ChatMessageBubble>
            ))
        ) : (
          <EmptyState onChoice={sendInitialQuestion} />
        )}
      </div>
      <InputGroup size="md" alignItems={"center"}>
        <AutoResizeTextarea
          value={input}
          maxRows={5}
          rounded={"md"}
          textColor={"white"}
          borderColor={"rgb(58, 58, 61)"}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              sendMessage();
            } else if (e.key === "Enter" && e.shiftKey) {
              e.preventDefault();
              setInput(input + "\n");
            }
          }}
        />
        <InputRightElement h="full" paddingRight={"15px"}>
          <IconButton
            colorScheme="blue"
            rounded={"full"}
            aria-label="Send"
            icon={isLoading ? <Spinner /> : <ArrowUpIcon />}
            type="submit"
            onClick={(e) => {
              e.preventDefault();
              sendMessage();
            }}
          />
        </InputRightElement>
      </InputGroup>
    </div>
  );
}
