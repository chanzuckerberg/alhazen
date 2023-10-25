/**
    * @description      : 
    * @author           : 
    * @group            : 
    * @created          : 24/10/2023 - 00:03:57
    * 
    * MODIFICATION LOG
    * - Version         : 1.0.0
    * - Date            : 24/10/2023
    * - Author          : 
    * - Modification    : 
**/
"use client";

import { ChatWindow } from "../app/components/ChatWindow";
import { ToastContainer } from "react-toastify";

import { ChakraProvider } from "@chakra-ui/react";

export default function Home() {
  return (
    <ChakraProvider>
      <ToastContainer />
      <ChatWindow
        titleText="Alhazen Scientific Research Assistant"
        placeholder="How can I help you?"
      ></ChatWindow>
    </ChakraProvider>
  );
}

