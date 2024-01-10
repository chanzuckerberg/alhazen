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

import { ChatWindow } from "./components/ChatWindow";
import { ToastContainer } from "react-toastify";
import { RecoilRoot } from "recoil";
import { EmailIcon } from "@chakra-ui/icons";
import { TopDashboard } from "./components/TopDashboard";

import {
  Box,
  ChakraProvider,
  Flex,
  Heading,
  Text,
  IconButton,
  Button,
  Stack,
  Collapse,
  Icon,
  Popover,
  PopoverTrigger,
  PopoverContent,
  useColorModeValue,
  useBreakpointValue,
  useDisclosure,
} from '@chakra-ui/react'
import {
  HamburgerIcon,
  CloseIcon,
  ChevronDownIcon,
  ChevronRightIcon,
} from '@chakra-ui/icons'
import SimpleNavBar from "./components/SimpleNavBar";

const Links = ['Dashboard', 'Projects', 'Team']
export default function Home() {
  return (
    <ChakraProvider>
      <ToastContainer />
      <RecoilRoot>
        <Flex flexDirection="column" width="100%">
          <SimpleNavBar />
        </Flex>
        <Flex>
        <Flex flexDirection="column" width="50%">
          <ChatWindow
            titleText="Alhazen Scientific Research Assistant"
            placeholder="How can I help you?"></ChatWindow>
        </Flex>
        <Flex flexDirection="column" width="50%">
        </Flex>
        </Flex>
        </RecoilRoot>
    </ChakraProvider>
  );
}

