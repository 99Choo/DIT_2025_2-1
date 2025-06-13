package com.example.albamanager;

public class ScheduleItem {
    String date;
    String time;
    String place;

    public ScheduleItem(String date, String time, String place) {
        this.date = date;
        this.time = time;
        this.place = place;
    }

    public String getDate() { return date; }
    public String getTime() { return time; }
    public String getPlace() { return place; }
}
