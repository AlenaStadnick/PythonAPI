package clickup.api.rest;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class AuthenticationRestClient extends BaseRestClient {

    public AuthenticationRestClient(){
        this.setUpRestAssured();
    }

    public Response getUser() {
        return RestAssured.given()
                .header("Authorization",  dotenv.get("TOKEN",System.getenv("TOKEN")))
                .get("/user");
    }

}