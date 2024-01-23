package com.example.helloworld;

import static org.hamcrest.Matchers.equalTo;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.junit.jupiter.api.Test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockHttpServletRequestBuilder;

@SpringBootTest
@AutoConfigureMockMvc
public class HelloWorldControllerTest {
    
    @Autowired
    private MockMvc mvc;

    @Test
    public void getHTTP() throws Exception {
        mvc.performMockMvcRequestBuilders.get("/").accept(MediaType.ALL).andExpect(content().string(equalTo("Hello World!")));
    }
}
