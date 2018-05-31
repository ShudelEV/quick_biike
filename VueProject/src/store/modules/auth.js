import Firebase from '../../api/firebase'

const state = {
    user: {
        loggedIn: false,
        uid: '',
        name: '',
        profilePicUrl: ''
    },
    error: ''
};

const mutations = {
    onAuthStateChanged (state, { user }) {
        state.user = user
    },

    setUser (state, { key, val }) {
        Vue.set(state.user, key, val)
    }
};

const actions = {
    onAuthStateChanged ({ commit }, user) {
        commit('onAuthStateChanged', { user })
    },

    signInGoogle () {
        Firebase.signInGoogle()
    },

    signOut () {
        Firebase.signOut()
    },

    setUserInfo ({ commit, state }, { key, val }) {
        return new Promise((resolve, reject) => {
            if (state.user.loggedIn) { // is signed in. Firebase
                Firebase.setUserInfo(key, val)
                    .then(() => {
                        commit('setUser', { key, val });
                        resolve()
                    }).catch(reject)
            } else { // is signed out. Localstorage
                reject('still dev for guest')
            }
        })
    },
};

const getters = {
    user: state => state.user,
    currentUserName: state => state.user.name,
    currentUserId: state => state.user.uid
};

export default {
    state,
    getters,
    actions,
    mutations
}

// export default {
//     namespaced: true,
//     state: {
//         user: {
//
//             loggedIn: false,
//             uid: '',
//             name: '',
//         },
//         error: '',
//         googleAuthProvider: googleAuthProvider,
//         facebookAuthProvider: facebookAuthProvider,
//         twitterAuthProvider: twitterAuthProvider,
//         githubAuthProvider: githubAuthProvider
//     },
//     mutations: {
//         logout(state) {
//             state.auth.signOut();
//         },
//         login(state, user) {
//             const promis = state.auth.signInWithEmailAndPassword(user.email, user.password);
//             promis.then((userResult) => {
//                 user.result(userResult);
//                 console.log("from Vuex : Done : " + user.email);
//             }).catch(error => {
//                 state.error = error.message;
//                 user.error(error)
//             })
//         },
//         signInGoogle(state, callBack) {
//             let provider = state.googleAuthProvider;
//             state.auth.signInWithPopup(provider).then((result) => {
//                 callBack.result(result)
//             }).catch((error) => {
//                 callBack.error(error)
//             });
//         },
//         signInFacebook(state, callBack) {
//             let provider = state.facebookAuthProvider;
//             state.auth.signInWithPopup(provider).then((result) => {
//                 callBack.result(result);
//             }).catch((error) => {
//                 callBack.error(error)
//             });
//         },
//         signInTwitter(state, callBack) {
//             let provider = state.twitterAuthProvider;
//             state.auth.signInWithPopup(provider).then((result) => {
//                 callBack.result(result);
//             }).catch((error) => {
//                 callBack.error(error)
//             });
//         },
//         signInGithub(state, callBack) {
//             let provider = state.githubAuthProvider;
//             state.auth.signInWithPopup(provider).then((result) => {
//                 callBack.result(result);
//             }).catch((error) => {
//                 callBack.error(error)
//             });
//         },
//         register(state, user) {
//             const promis = state.auth.createUserWithEmailAndPassword(user.email, user.password);
//             promis.then((userResult) => {
//                 console.log("from Vuex : Done : " + user.email);
//                 user.result(userResult)
//             }).catch(error => {
//                 state.error = error.message;
//                 user.error(error)
//             })
//         },
//         updateProfilePicture(state, image) {
//             state.auth.currentUser.updateProfile({
//                 photoURL: image.ref
//             }).then(() => {
//                 image.result()
//             }).catch(error => {
//                 image.error(error)
//             })
//         },
//         stateChanged(state, callBack) {
//             state.auth.onAuthStateChanged((user) => {
//                 if (user) {
//                     callBack.then(user)
//                 } else {
//                     callBack.catch()
//                 }
//             })
//         }
//     },
//     getters: {},
//     actions: {}
// }
