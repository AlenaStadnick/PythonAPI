package clickup.api.steps;

import clickup.api.utils.RandomData;
import clickup.api.utils.ResourceUtils;
import io.cucumber.java.en.And;
import io.restassured.response.Response;
import org.json.JSONObject;
import org.openqa.selenium.json.Json;

import java.util.Random;

public class AuthenticationSteps extends BaseSteps {
    RandomData randomData = new RandomData();
    @And("Get user info")
    public void getUser() {
        final Response getUserResponse = authenticationRestClient.getUser();
        sharedTestData.setResponse(getUserResponse);
    }

    @And("Create folder from file {}")
    public void createFolderFromFile(String path) {
        String name = "my folder" + randomData.generateRandomString(5);
        System.out.println("chvrifhioaviodfionvfionnnv");
        System.out.println(name);
        String source = "data/folders/" + path;
        JSONObject body = ResourceUtils.readJson(source);
        body.put("name", name );
        System.out.println( body.toString());
        final Response createFolderResponse = foldersRestClient.createFolderFromFile(body);
        sharedTestData.setResponse(createFolderResponse);
        System.out.println(createFolderResponse);
    }

    @And("Update folder with id {}")
    public void updateFolderWithName(String id) {
        String name = "my folder updated " + randomData.generateRandomString(10);
        JSONObject requestParams = new JSONObject();
        requestParams.put("name", name );
        final Response createFolderResponse = foldersRestClient.updateFolderIdWithBody(sharedTestData.getDataFromMap(id), requestParams);
        sharedTestData.setResponse(createFolderResponse);
    }

}
