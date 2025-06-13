package com.example.albamanager;

import androidx.room.Dao;
import androidx.room.Insert;
import androidx.room.Query;

import java.util.List;

@Dao
public interface ScheduleDao {
    @Insert
    void insert(ScheduleEntity schedule);

    @Query("SELECT * FROM schedule_table ORDER BY id DESC")
    List<ScheduleEntity> getAll();
}
