package clickup.api.steps;

import clickup.api.steps.BaseSteps;
import io.cucumber.java.en.And;
import io.restassured.filter.log.LogDetail;
import org.assertj.core.api.Assertions;

public class ResponseSteps extends BaseSteps {

    @And("Response status should be {}")
    public void responseStatusShouldBe(final int statusCode) {
        sharedTestData.getResponse().getBody().print();
        sharedTestData.getResponse().then().log().ifValidationFails(LogDetail.BODY).statusCode(statusCode);
    }

    @And("User save response body")
    public void saveResponseBody() {
        sharedTestData.setResponseBody(sharedTestData.getResponse().getBody().asPrettyString());
    }

    @And("User store {} from body as {}")
    public void storeDataFromBody(String data, String variableName) {
        String value = sharedTestData.getResponse().jsonPath().get(data);
        System.out.println(value);
        System.out.println(variableName);
        sharedTestData.setDataToMap(variableName, value);
    }

}
