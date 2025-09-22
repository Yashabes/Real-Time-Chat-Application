package com.grewal.realtimechatapp.controller;

import com.grewal.realtimechatapp.model.ChatMessage;
import com.grewal.realtimechatapp.repository.ChatMessageRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class MessageController {
    private final ChatMessageRepository chatMessageRepository;

    public ResponseEntity<List<ChatMessage>> getPrivateMessages(@RequestParam String user1,
                                                                @RequestParam String user2) {
        List<ChatMessage> messages = chatMessageRepository.findPrivateMessagesBetweenTwoUsers(user1, user2);
        return ResponseEntity.ok(messages);
    }
}
