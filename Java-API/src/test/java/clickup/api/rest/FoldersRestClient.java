package clickup.api.rest;

import com.google.gson.JsonObject;
import io.cucumber.java.en.And;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.json.JSONObject;

public class FoldersRestClient extends BaseRestClient {

public FoldersRestClient(){
    this.setUpRestAssured();
}

    public Response createFolderFromFile(JSONObject body) {

        return RestAssured.given()
                .header("Authorization",  dotenv.get("TOKEN"))
                .contentType(ContentType.JSON)
                .body(body.toString())
                .post("/space/90151393719/folder");
    }

}