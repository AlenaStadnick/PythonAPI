package clickup.api.rest;

import io.restassured.response.Response;
import io.restassured.matcher.RestAssuredMatchers.*;
import org.hamcrest.Matchers.*;

import static org.hamcrest.CoreMatchers.containsString;
import static org.hamcrest.Matchers.equalTo;

public class AuthenticationRestClient extends BaseRestClient {

    public AuthenticationRestClient(){
        this.setUpRestAssured();
    }

    public Response getUser() {
        Response getUser = requestSpec
                .get("/user");
//        getUser.then().body("user.username", equalTo(2));
        return getUser;
    }

}