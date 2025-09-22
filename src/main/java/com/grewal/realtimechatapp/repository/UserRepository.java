package com.grewal.realtimechatapp.repository;

import com.grewal.realtimechatapp.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

@Repository
public interface UserRepository extends JpaRepository<User,Long> {
    boolean existsByUsername(String username);
    @Transactional
    @Modifying
    @Query("UPDATE User u SET u.isOnline= :isOnline WHERE u.username= :username")
    void updateUserOnlineStatus(@Param("username") String username, @Param("isOnline") boolean isOnline);
}
