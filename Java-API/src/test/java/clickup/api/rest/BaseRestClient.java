package clickup.api.rest;

import io.github.cdimascio.dotenv.Dotenv;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.specification.RequestSpecification;
import org.junit.runner.Request;

public abstract class BaseRestClient {
    Dotenv dotenv = Dotenv.configure().ignoreIfMissing().load();
protected RequestSpecification requestSpec;
    public void setUpRestAssured() {
//        RestAssured.baseURI = dotenv.get("BASE_URL");
        this.requestSpec = RestAssured.given()
                .baseUri(dotenv.get("BASE_URL"))
                .contentType(ContentType.JSON)
                .header("Authorization", dotenv.get("TOKEN"));
    }

    ;
}
