package com.example.albamanager;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.List;

public class ScheduleActivity extends AppCompatActivity {

    private EditText editDate, editTime, editPlace;
    private Button btnSave;
    private RecyclerView recyclerView;
    private ScheduleAdapter adapter;
    private final List<ScheduleItem> scheduleList = new ArrayList<>(); // 고정 목록

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_schedule);

        // 뷰 바인딩
        editDate = findViewById(R.id.edit_date);
        editTime = findViewById(R.id.edit_time);
        editPlace = findViewById(R.id.edit_place);
        btnSave = findViewById(R.id.btn_save);
        recyclerView = findViewById(R.id.recycler_schedule);

        // 리사이클러뷰 설정
        adapter = new ScheduleAdapter(scheduleList);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(adapter);

        // DB 인스턴스
        ScheduleDatabase db = ScheduleDatabase.getInstance(this);

        // 저장 버튼 클릭 시
        btnSave.setOnClickListener(v -> {
            String date = editDate.getText().toString();
            String time = editTime.getText().toString();
            String place = editPlace.getText().toString();

            if (!date.isEmpty() && !time.isEmpty() && !place.isEmpty()) {
                // ScheduleItem 추가
                ScheduleItem item = new ScheduleItem(date, time, place);
                scheduleList.add(item);

                // DB에 ScheduleEntity 저장
                ScheduleEntity entity = new ScheduleEntity(date, time, place);
                db.scheduleDao().insert(entity);

                adapter.notifyDataSetChanged();

                // 입력 필드 초기화
                editDate.setText("");
                editTime.setText("");
                editPlace.setText("");
            }
        });

        // DB에서 기존 데이터 불러오기
        List<ScheduleEntity> entities = db.scheduleDao().getAll();
        for (ScheduleEntity entity : entities) {
            scheduleList.add(new ScheduleItem(entity.getDate(), entity.getTime(), entity.getPlace()));
        }
        adapter.notifyDataSetChanged();
    }
}
