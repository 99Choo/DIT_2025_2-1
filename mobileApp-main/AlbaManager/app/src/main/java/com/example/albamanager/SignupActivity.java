
package com.example.albamanager;

import android.content.ContentValues;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.text.TextUtils;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.albamanager.DBHelper;

public class SignupActivity extends AppCompatActivity {

    private EditText editId, editPassword, editName;
    private Button btnSignup;
    private DBHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);

        editId = findViewById(R.id.edit_signup_id);
        editPassword = findViewById(R.id.edit_signup_password);
        editName = findViewById(R.id.edit_signup_name);
        btnSignup = findViewById(R.id.btn_signup_confirm);

        dbHelper = new DBHelper(this);

        btnSignup.setOnClickListener(view -> {
            String id = editId.getText().toString();
            String password = editPassword.getText().toString();
            String name = editName.getText().toString();

            if (TextUtils.isEmpty(id) || TextUtils.isEmpty(password) || TextUtils.isEmpty(name)) {
                Toast.makeText(this, "모든 정보를 입력해주세요.", Toast.LENGTH_SHORT).show();
                return;
            }

            SQLiteDatabase db = dbHelper.getWritableDatabase();
            ContentValues values = new ContentValues();
            values.put("userId", id);
            values.put("password", password);
            values.put("name", name);

            long result = db.insert("user", null, values);
            if (result == -1) {
                Toast.makeText(this, "회원가입 실패", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(this, "회원가입 성공", Toast.LENGTH_SHORT).show();
                finish();
            }
        });
    }
}
