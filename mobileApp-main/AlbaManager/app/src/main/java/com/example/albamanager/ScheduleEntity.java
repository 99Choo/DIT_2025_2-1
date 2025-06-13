package com.example.albamanager;

import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity(tableName = "schedule_table")
public class ScheduleEntity {
    @PrimaryKey(autoGenerate = true)
    public int id;

    public String date;
    public String time;
    public String place;

    public ScheduleEntity(String date, String time, String place) {
        this.date = date;
        this.time = time;
        this.place = place;
    }

    // ✅ ScheduleActivity에서 사용될 getter 메서드 추가
    public String getDate() {
        return date;
    }

    public String getTime() {
        return time;
    }

    public String getPlace() {
        return place;
    }
}
