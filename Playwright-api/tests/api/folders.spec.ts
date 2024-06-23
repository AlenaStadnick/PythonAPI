import {test, expect, APIResponse} from '@playwright/test';

test.describe('try api', async () => {
  let id:string
  let getFolders;

  test('should create a bug report', async ({ request }) => {
    await  test.step('get data from folder', async  ()=>{
       getFolders = await request.get('space/90152363684/folder')
    })

    test.step('Assert all data', async  ()=> {
      expect(await getFolders.json()).toBeTruthy();

      expect(getFolders.status()).toBe(200);
      const data = await getFolders.json();
      id = data.folders[0].id;
      expect(id).toBeDefined()
    })
  });

  test('get folder', async ({ request }) => {
    let getFolder:APIResponse;
    await  test.step('get data from folder', async ()=>{
      getFolder = await request.get('space/90152363684/folder')
    })
    const datas = await getFolder.json();
    await  getFolder.text()
    id = datas.folders[0].id;
    test.info().annotations.push({ type: 'id', description: id });
    test.info().annotations.push({ type: 'body', description: await getFolder.text() });

    const getFolders = await request.get(`folder/${id}`)
    expect(getFolders.json()).toBeTruthy();

    expect(getFolders.status()).toBe(200);
    const data = await getFolders.json();
    id = data.id;
    expect(id).toBeDefined()
  });

});


