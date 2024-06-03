package clickup.api.rest;

import io.github.cdimascio.dotenv.Dotenv;
import io.restassured.RestAssured;

public abstract class BaseRestClient {
    Dotenv dotenv = Dotenv.load();

    public void setUpRestAssured() {
    try{
        Dotenv dotenv = Dotenv.configure().ignoreIfMissing().load();
        RestAssured.baseURI = dotenv.get("BASE_URL",System.getenv("BASE_URL"));
    };
};
