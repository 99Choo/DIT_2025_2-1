package com.example.albamanager;

import android.content.Context;

import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;

@Database(entities = {ScheduleEntity.class}, version = 1)
public abstract class ScheduleDatabase extends RoomDatabase {
    private static ScheduleDatabase instance;

    public abstract ScheduleDao scheduleDao();

    public static synchronized ScheduleDatabase getInstance(Context context) {
        if (instance == null) {
            instance = Room.databaseBuilder(context.getApplicationContext(),
                            ScheduleDatabase.class, "schedule_db")
                    .allowMainThreadQueries() // 나중에 코루틴으로 바꿀 수도 있음
                    .build();
        }
        return instance;
    }
}

