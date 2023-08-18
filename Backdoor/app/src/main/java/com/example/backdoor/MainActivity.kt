package com.example.backdoor

import android.content.ContentValues.TAG
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley

class MainActivity : AppCompatActivity() {
    private var mRequestQueue: RequestQueue? = null
    private var mStringRequest: StringRequest? = null
    private val url = "https://run.mocky.io/v3/85cf9aaf-aa4f-41bf-b10c-308f032f7ccc"
    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        getData()
    }
    private fun getData() {
        // RequestQueue initialized
        mRequestQueue = Volley.newRequestQueue(this)

        // String Request initialized
        mStringRequest = StringRequest(
            Request.Method.GET, url,
            { response ->
                Toast.makeText(applicationContext, "Response :$response", Toast.LENGTH_LONG)
                    .show() //display the response on screen
            }
        ) { error -> Log.i(TAG, "Error :$error") }
        mRequestQueue!!.add(mStringRequest)
    }
}