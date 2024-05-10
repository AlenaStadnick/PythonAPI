package clickup.api.steps;

import clickup.api.utils.ResourceUtils;
import io.cucumber.java.en.And;
import io.restassured.response.Response;

public class AuthenticationSteps extends BaseSteps {

    @And("Get user info")
    public void getUser() {
        final Response getUserResponse = authenticationRestClient.getUser();
        sharedTestData.setResponse(getUserResponse);
    }

    @And("Create folder from file {}")
    public void createFolderFromFile(String path) {
        String source = "data/folders/" + path;
        final Response createFolderResponse = foldersRestClient.createFolderFromFile(ResourceUtils.readJson(source));
        sharedTestData.setResponse(createFolderResponse);
    }

}
