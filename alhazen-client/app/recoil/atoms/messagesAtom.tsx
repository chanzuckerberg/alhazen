/**
    * @description      : 
    * @author           : 
    * @group            : 
    * @created          : 01/12/2023 - 14:16:30
    * 
    * MODIFICATION LOG
    * - Version         : 1.0.0
    * - Date            : 01/12/2023
    * - Author          : 
    * - Modification    : 
**/
import { atom } from "recoil";
import { Message } from "../../components/ChatMessageBubble";

export const messagesAtom = atom({
    key: "messagesState",
    default: [] as Array<Message>,
  });