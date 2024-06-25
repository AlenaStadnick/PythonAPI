package clickup.api.rest;

import io.github.cdimascio.dotenv.Dotenv;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.json.JSONObject;

public class FoldersRestClient extends BaseRestClient {

public FoldersRestClient(){
    this.setUpRestAssured();
}

    public Response createFolderFromFile(JSONObject body) {
        System.out.println("Request Body: " + body.toString());

        return requestSpec
                .body(body.toString())
                .post("/space/90151393719/folder");
    }

    public Response updateFolderIdWithBody(String id, JSONObject body) {
//        System.out.println("Request Body: " + body.toString());

        return requestSpec
                .body(body.toString()).log().body()
                .put(String.format("/space/90151393719/folder/%s", id));
    }

}