/**
    * @description      : 
    * @author           : 
    * @group            : 
    * @created          : 27/11/2023 - 23:19:05
    * 
    * MODIFICATION LOG
    * - Version         : 1.0.0
    * - Date            : 27/11/2023
    * - Author          : 
    * - Modification    : 
**/
import { MouseEvent, MouseEventHandler } from "react";
import {
  Heading,
  Link,
  Card,
  CardHeader,
  Flex,
  Spacer,
} from "@chakra-ui/react";
import { ExternalLinkIcon } from "@chakra-ui/icons";

export function EmptyState(props: { onChoice: (question: string) => any }) {
  const handleClick = (e: MouseEvent) => {
    props.onChoice((e.target as HTMLDivElement).innerText);
  };
  return (
    <div className="rounded flex flex-col items-center max-w-full md:p-8">
      <Heading fontSize="3xl" fontWeight={"medium"} mb={1} color={"white"}>
        Alhazen Scientific Research Assistant 
      </Heading>
      <Heading
        fontSize="xl"
        fontWeight={"normal"}
        mb={1}
        color={"white"}
        marginTop={"10px"}
        textAlign={"center"}
      >
        I am 'Alhazen', an AI-powered scientific research assistant with a new twist:
      </Heading>
      <Heading
        fontSize="xl"
        fontWeight={"normal"}
        mb={1}
        color={"white"}
        marginTop={"10px"}
        textAlign={"center"}
      >

        I respond to your inquiries by developing a local library of research articles, reviews, online documents, and database records and read them in detail.
        I will prepare notes, reports, and summaries of the information I find and present them to you in a way that is easy to understand.   
        </Heading>
      <Heading
        fontSize="xl"
        fontWeight={"normal"}
        mb={1}
        color={"white"}
        marginTop={"10px"}
        textAlign={"center"}
      >
        My goal is to help you more easily explore, understand, and engage with the all the complexities of existing scientific knowledge in areas that you may not be familiar with.
      </Heading>      
      <Heading
        fontSize="xl"
        fontWeight={"normal"}
        mb={1}
        color={"white"}
        marginTop={"10px"}
        textAlign={"center"}
      >
        What are some high-level goals that you'd like to pursue by building a detailed knowledge base around?.
      </Heading>      

      <Flex marginTop={"25px"} grow={1} maxWidth={"800px"} width={"100%"}>
        <Card
          onMouseUp={handleClick}
          width={"48%"}
          backgroundColor={"rgb(58, 58, 61)"}
          _hover={{ backgroundColor: "rgb(78,78,81)" }}
          cursor={"pointer"}
          justifyContent={"center"}
        >
          <CardHeader justifyContent={"center"}>
            <Heading
              fontSize="lg"
              fontWeight={"medium"}
              mb={1}
              color={"gray.200"}
              textAlign={"center"}
            >
              What new imaging biological microscopy methods have emerged in the last five years?
            </Heading>
          </CardHeader>
        </Card>
        <Spacer />
        <Card
          onMouseUp={handleClick}
          width={"48%"}
          backgroundColor={"rgb(58, 58, 61)"}
          _hover={{ backgroundColor: "rgb(78,78,81)" }}
          cursor={"pointer"}
          justifyContent={"center"}
        >
          <CardHeader justifyContent={"center"}>
            <Heading
              fontSize="lg"
              fontWeight={"medium"}
              mb={1}
              color={"gray.200"}
              textAlign={"center"}
            >
              Build a detailed review of all available CryoET experiments, detailing the various classes of metadata being used in each step.
            </Heading>
          </CardHeader>
        </Card>
      </Flex>
      <Flex marginTop={"25px"} grow={1} maxWidth={"800px"} width={"100%"}>
        <Card
          onMouseUp={handleClick}
          width={"48%"}
          backgroundColor={"rgb(58, 58, 61)"}
          _hover={{ backgroundColor: "rgb(78,78,81)" }}
          cursor={"pointer"}
          justifyContent={"center"}
        >
          <CardHeader justifyContent={"center"}>
            <Heading
              fontSize="lg"
              fontWeight={"medium"}
              mb={1}
              color={"gray.200"}
              textAlign={"center"}
            >
              Which research groups and/or scientists are most prevalent across all fields of microscopy research who also work in Africa?
            </Heading>
          </CardHeader>
        </Card>
        <Spacer />
        <Card
          onMouseUp={handleClick}
          width={"48%"}
          backgroundColor={"rgb(58, 58, 61)"}
          _hover={{ backgroundColor: "rgb(78,78,81)" }}
          cursor={"pointer"}
          justifyContent={"center"}
        >
          <CardHeader justifyContent={"center"}>
            <Heading
              fontSize="lg"
              fontWeight={"medium"}
              mb={1}
              color={"gray.200"}
              textAlign={"center"}
            >
              Write a detailed review of the latest research involving AI and generative machine learning in biology.
            </Heading>
          </CardHeader>
        </Card>
      </Flex>
      <Heading
        fontSize="m"
        fontWeight={"normal"}
        mb={1}
        color={"white"}
        marginTop={"10px"}
        textAlign={"center"}
      >
        Built on LangChain 🦜🔗
      </Heading>
    </div>
  );
}
