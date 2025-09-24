package com.grewal.realtimechatapp.model;

import jakarta.persistence.*;
import lombok.Data;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Collection;
import java.util.List;

@Entity
@Data
@Table(name = "users")
public class User{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(nullable = false,  unique = true)
    private String username;
    @Column(nullable = false)
    private String password;
    @Column(nullable = false,   unique = true)
    private String email;
    @Column(nullable = false,   name = "is_online")
    private boolean isOnline;
}
