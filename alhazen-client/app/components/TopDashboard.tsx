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

export function TopDashboard(props: {}) {
  return (
    <div className="rounded flex flex-col items-center max-w-full md:p-8">
        <Heading fontSize="3xl" fontWeight={"medium"} mb={1} color={"white"}>
          Placeholder 
        </Heading>
    </div>
    );
}
