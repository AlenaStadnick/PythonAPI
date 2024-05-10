package clickup.api.steps;

import clickup.api.data.SharedTestData;
import clickup.api.rest.AuthenticationRestClient;
import clickup.api.rest.FoldersRestClient;

public abstract class BaseSteps {
    protected static SharedTestData sharedTestData = new SharedTestData();
    protected static AuthenticationRestClient authenticationRestClient = new AuthenticationRestClient();
    protected final FoldersRestClient foldersRestClient = new FoldersRestClient();

}
