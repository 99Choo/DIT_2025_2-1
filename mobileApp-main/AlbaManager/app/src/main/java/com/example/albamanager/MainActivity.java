package com.example.albamanager;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private TextView tvTodaySchedule;
    private Button btnSchedule, btnSalary, btnBoard, btnSettings;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvTodaySchedule = findViewById(R.id.tv_today_schedule);
        btnSchedule = findViewById(R.id.btn_schedule);
        btnSalary = findViewById(R.id.btn_salary);
        btnBoard = findViewById(R.id.btn_board);
        btnSettings = findViewById(R.id.btn_settings);

        // 샘플 데이터 표시
        tvTodaySchedule.setText("오늘 알바: 15:00 ~ 20:00 GS25");

        // 버튼 이벤트 설정
        btnSchedule.setOnClickListener(v -> {
            // 예: startActivity(new Intent(this, ScheduleActivity.class));
        });

        btnSalary.setOnClickListener(v -> {
            // 예: startActivity(new Intent(this, SalaryActivity.class));
        });

        btnBoard.setOnClickListener(v -> {
            // 예: startActivity(new Intent(this, BoardActivity.class));
        });

        btnSettings.setOnClickListener(v -> {
            // 예: startActivity(new Intent(this, SettingsActivity.class));
        });
    }
}
