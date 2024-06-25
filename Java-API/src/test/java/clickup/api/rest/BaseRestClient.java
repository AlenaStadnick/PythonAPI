package clickup.api.rest;

import io.github.cdimascio.dotenv.Dotenv;
import io.restassured.RestAssured;

public abstract class BaseRestClient {
    Dotenv dotenv = Dotenv.configure().ignoreIfMissing().load();

    public void setUpRestAssured() {
        RestAssured.baseURI = dotenv.get("BASE_URL");
    }

    ;
}
